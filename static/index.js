function submitFormReviewAdd(event) {
  event.preventDefault();

  const customerName = document.getElementById('customer_name_add').value;
  const customerSurname = document.getElementById('customer_surname_add').value;
  const reviewText = document.getElementById('review_text').value;

  const payload = { customerName, customerSurname, reviewText };

  fetch('/submit_review', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
    .then((response) => response.json())
    .then((data) => {
      const outputDiv = document.getElementById('output');
      outputDiv.innerHTML = data["status"];
    })
    .catch((error) => console.error(error));
}

function submitFormReviewFind(event) {
  event.preventDefault();

  const customerName = document.getElementById('customer_name_find').value;
  const customerSurname = document.getElementById('customer_surname_find').value;
  const payload = { customerName, customerSurname};

  fetch('/find_review', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
    .then((response) => response.json())
    .then((data) => {
      const outputDiv = document.getElementById('output');
      outputDiv.innerHTML = data["status"];
    })
    .catch((error) => console.error(error));
}

function submitFormCustomerAdd(event) {
  event.preventDefault();
  const customerName = document.getElementById('customer_name_add').value;
  const customerSurname = document.getElementById('customer_surname_add').value;
  const shiftTeamId = document.getElementById('shift_team_add').value;

  const payload = { customerName, customerSurname, shiftTeamId};
  console.log(customerName)
  console.log(customerSurname)
  console.log(shiftTeamId)
  fetch('/add_customer', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
    .then((response) => response.json())
    .then((data) => {
      const outputDiv = document.getElementById('output');
      outputDiv.innerHTML = data["status"];
    })
    .catch((error) => console.error(error));
}


function submitFormReviewDelete(event) {
  event.preventDefault();
  const customerName = document.getElementById('customer_name_delete').value;
  const customerSurname = document.getElementById('customer_surname_delete').value;
  const payload = { customerName, customerSurname};

  fetch('/delete_review', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
    .then((response) => response.json())
    .then((data) => {
      const outputDiv = document.getElementById('output');
      outputDiv.innerHTML = data["status"];
    })
    .catch((error) => console.error(error));
}

function submitFormCustomerOrderUpdate(event) {
  event.preventDefault();
  const orderId = document.getElementById('order_id').value;
  const status = document.getElementById('status').value;
  const payload = { orderId, status};

  fetch('/update_order', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
    .then((response) => response.json())
    .then((data) => {
      const outputDiv = document.getElementById('output');
      outputDiv.innerHTML = data["status"];
    })
    .catch((error) => console.error(error));
}

function submitFormManager(event) {
  event.preventDefault();
  const distributorId = document.getElementById('distributor_id').value;
  const payload = {distributorId};

  fetch('/get_distributor_medicines', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
    .then((response) => response.json())
    .then((data) => {
      const outputDiv = document.getElementById('output');
      outputDiv.innerHTML = data["status"];
    })
    .catch((error) => console.error(error));
}
