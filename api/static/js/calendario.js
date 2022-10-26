let modal = new bootstrap.Modal(document.getElementById('myModal'))

document.addEventListener('DOMContentLoaded', function () {
  let calendarUi = document.getElementById('calendario');
  let calendar = new FullCalendar.Calendar(calendarUi, {
    initialView: 'dayGridMonth',
    locale: 'es',
    headerToolbar: {
      left: 'prev,next,today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,listWeek'
    },
    dateClick: function (info) {
      document.getElementById('id_fecha').value = info.dateStr
      console.log(info.dateStr)
      modal.show()
    },
  });
  calendar.render();

})
// function guardar () {
//   // let formData = new FormData();
//   // formData.append('title', $('#title').val().trim());
//   const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

//   const request = $.ajax({
    
//     type: "POST",
//     url: "/api/actividades/",
//     datatype:'json',
//     data: $('#formulario').serialize(),
//     body:formulario,
//     header:{
//       'X-CSRFToken': csrftoken
//     },

//     success: function (data) {
//       alert(data)
//     }
//   });
//   request.done(function (response) {
  
//     // Cierra el modal, oculta el identificador eliminado, etc.
//   });

//   function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// const cargarGestor =async()=>{


//     request.done(function(response) {
//        window.location.reload()
//         modal.hidden()
//     });
//     }

// window.addEventListener('load',async ()=>{
// cargarGestor()
// })
