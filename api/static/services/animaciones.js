// $(document).ready(function () {
//     var percent = 0;

//     timerId = setInterval(function () {
//         //increment progress bar
//         percent += 5;
//         $('.progress-bar ').css('width', percent + '%');
//         $('.progress-bar ').attr('aria-valuenow', percent);
//         $('.progress-bar ').text(percent + '%');
//        let proceso = $('#proceso').text()

//        console.log(proceso)


//         if($('#proceso').html()==='40%'){
//             if (percent == 40) {
//               clearInterval(timerId);
//               $('.proceso').show();
//           }
//       }
//         if($('#abierto').html()==='10%'){
//           if (percent == 0) {
//             clearInterval(timerId);
//             $('.abierto').show();
//         }
//     }
//         else if (percent == 100) {
//             clearInterval(timerId);
//             $('.finalizado').show();
//         }

//     }, 1000);
// });