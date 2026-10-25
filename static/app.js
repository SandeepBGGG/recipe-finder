const form = document.querySelector('#search-form');
const input = document.querySelector('#ingredients');
document.querySelectorAll('.example').forEach(button => {
  button.addEventListener('click', () => {
    input.value = button.dataset.ingredients;
    input.focus();
    form.requestSubmit();
  });
});
form.addEventListener('submit', () => {
  const button = document.querySelector('#find-button');
  button.disabled = true;
  button.textContent = 'Finding recipes…';
  form.setAttribute('aria-busy', 'true');
});
window.addEventListener('pageshow', () => {
  const button = document.querySelector('#find-button');
  button.disabled = false;
  button.innerHTML = 'Find recipes <span aria-hidden="true">↗</span>';
  form.removeAttribute('aria-busy');
});
