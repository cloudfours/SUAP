let modal = new bootstrap.Modal(document.getElementById('myModal'))

// document.addEventListener('DOMContentLoaded', function () {
//   let calendarUi = document.getElementById('calendario');
//   let calendar = new FullCalendar.Calendar(calendarUi, {
//     initialView: 'dayGridMonth',
//     locale: 'es',
//     headerToolbar: {
//       left: 'prev,next,today',
//       center: 'title',
//       right: 'dayGridMonth,timeGridWeek,listWeek'
//     },
//     events:'/api/gestor/',
//     dateClick: function (info) {
//       document.getElementById('id_fecha').value = info.dateStr
//       console.log(info.dateStr)
//       modal.show()
//     },
   
//   });
//   calendar.render();

// })


// const cargarfechas=async()=>{
 
//  let response= await fetch('/api/gestor/')
//  let data = await  response.json()
// return data

  
// }
// // const cargarGestor =async()=>{


// //     request.done(function(response) {
// //        window.location.reload()
// //         modal.hidden()
// //     });
// //     }

// window.addEventListener('load',async()=>{
// await cargarfechas()
// })
