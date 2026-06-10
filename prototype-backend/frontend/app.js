const form = document.getElementById('patient-form');
const messageEl = document.getElementById('registration-message');
const searchButton = document.getElementById('search-button');
const queryInput = document.getElementById('search-query');
const searchMessageEl = document.getElementById('search-message');
const resultsBody = document.querySelector('#results-table tbody');

const resetMessage = (element) => {
  element.textContent = '';
};

const showMessage = (element, text, isError = false) => {
  element.textContent = text;
  element.style.color = isError ? '#b91c1c' : '#0f172a';
};

const renderResults = (patients) => {
  resultsBody.innerHTML = '';
  if (!patients.length) {
    resultsBody.innerHTML = '<tr><td colspan="5">No patients found.</td></tr>';
    return;
  }

  patients.forEach((patient) => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${patient.nhi || '-'}</td>
      <td>${patient.full_name}</td>
      <td>${patient.date_of_birth}</td>
      <td>${patient.sex || '-'}</td>
      <td>${patient.region || '-'}</td>
    `;
    resultsBody.appendChild(row);
  });
};

const postPatient = async (payload) => {
  const response = await fetch('/patients', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  return response.json().then((data) => ({ status: response.status, data }));
};

const fetchPatients = async (query) => {
  const url = new URL('/patients', window.location.origin);
  if (query) url.searchParams.set('q', query);
  const response = await fetch(url);
  return response.json();
};

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  resetMessage(messageEl);

  const formData = new FormData(form);
  const payload = {
    full_name: formData.get('full_name') || '',
    date_of_birth: formData.get('date_of_birth') || '',
    sex: formData.get('sex') || undefined,
    region: formData.get('region') || undefined,
    district: formData.get('district') || undefined,
    contact: formData.get('contact') || undefined,
  };

  try {
    const result = await postPatient(payload);
    if (result.status === 200) {
      showMessage(messageEl, `Patient registered with NHI ${result.data.nhi}`);
      form.reset();
      const query = queryInput.value.trim();
      const patients = await fetchPatients(query);
      renderResults(patients);
    } else {
      showMessage(messageEl, result.data.detail || 'Failed to register patient.', true);
    }
  } catch (error) {
    showMessage(messageEl, 'Unable to reach the API. Please try again.', true);
  }
});

searchButton.addEventListener('click', async () => {
  resetMessage(searchMessageEl);
  const query = queryInput.value.trim();

  try {
    const patients = await fetchPatients(query);
    renderResults(patients);
    if (!patients.length) showMessage(searchMessageEl, 'No matching patients were found.');
  } catch (error) {
    showMessage(searchMessageEl, 'Unable to fetch patients. Please try again.', true);
  }
});

window.addEventListener('load', async () => {
  const patients = await fetchPatients('');
  renderResults(patients);
});
