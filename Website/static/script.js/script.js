
function navigateToPage(event) {
  event.preventDefault();

  
  const targetPageURL = event.target.href;

 
  const buttonsAndLinks = document.querySelectorAll('button, a:not(.dropbtn)');
  buttonsAndLinks.forEach(element => {
    element.classList.add('fade-out');
  });

  
  setTimeout(() => {
   
    window.location.href = targetPageURL;
  }, 200); 
}

const buttonsAndLinks = document.querySelectorAll('button, a:not(.dropbtn)');
buttonsAndLinks.forEach(element => {
  element.addEventListener('click', navigateToPage);
});

document.addEventListener('DOMContentLoaded', () => {
  const buttonsAndLinks = document.querySelectorAll('button, a:not(.dropbtn)');
  buttonsAndLinks.forEach(element => {
    element.classList.add('fade-in');
  });
});
