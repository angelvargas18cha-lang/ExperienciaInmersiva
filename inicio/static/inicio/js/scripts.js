document.addEventListener("DOMContentLoaded", function () {
    const stars = document.querySelectorAll('.star-input');
    const input = document.getElementById('calificacion');
    const form = document.querySelector("form");

    // 🔥 Recuperar la última calificación guardada en localStorage (si existe)
    const saved = localStorage.getItem("calificacion");

    if (saved) {
        input.value = saved; // Asignamos el valor al input
        // Pintamos las estrellas basadas en el valor guardado
    }

    // Función para pintar las estrellas según la calificación
    function pintar(val) {
        stars.forEach(s => {
            s.classList.remove('filled');
            if (s.dataset.value <= val) {
                s.classList.add('filled');
            }
        });
    }

    // Evento cuando el usuario hace clic en una estrella
    stars.forEach(star => {
        star.addEventListener('click', function () {
            const value = this.dataset.value;
            input.value = value; // Asignamos el valor al input
            localStorage.setItem("calificacion", value); // Guardamos la calificación en localStorage
            pintar(value); // Pintamos las estrellas basadas en la calificación seleccionada
        });
    });

    // Limpiar las estrellas cuando se envíe el formulario
    form.addEventListener('submit', function () {
        localStorage.removeItem("calificacion"); // Limpiar la calificación de localStorage
        setTimeout(() => {
            pintar(0); // Restablecer las estrellas a su estado inicial (vacías)
        }, 500); // Esperamos medio segundo para que el formulario se envíe antes de limpiar
    });
});

// MENU RESPONSIVE


document.addEventListener("DOMContentLoaded", function() {
  const menuBtn = document.getElementById("mobile-menu");
  const navMenu = document.querySelector(".navbar-nav");

  if (menuBtn && navMenu) {
    menuBtn.addEventListener("click", function() {
      console.log("¡Botón clickeado!"); // Verifica si el botón de hamburguesa fue clickeado
      menuBtn.classList.toggle("is-active");
      navMenu.classList.toggle("active");
    });
  } else {
    console.error("No se encontraron los elementos del menú");
  }
});