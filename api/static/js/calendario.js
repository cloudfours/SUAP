// let insertar = new bootstrap.Modal(document.getElementById('myModal'))
// function abrir(){

//     insertar.modal('show');


// }
$(document).ready(function () {
  let table =$('#calendar').DataTable({"language": {
      "url": "//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json"},
      responsive:true,
    
    })
  $('#calendar').DataTable();
  new $.fn.dataTable.FixedHeader( table );


})
