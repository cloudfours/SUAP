$(document).ready(function () {
    let table =$('#example').DataTable({"language": {
        "url": "//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json"}
      })
    $('#example').DataTable();
    $('#caso').keyup(function(){
        table.column($(this).data('index')).search(this.value).draw();
    })
    $('#nombrecompleto').keyup(function(){
        table.column($(this).data('index')).search(this.value).draw();
    })
    $('#estado').click(function(){
        table.column($(this).data('index')).search(this.value).draw();
    })
    $('#identificacion').keyup(function(){
        table.column($(this).data('index')).search(this.value).draw();
    })
 


})
