$(document).ready(function () {
    let table =$('#example').DataTable()
    $('#example').DataTable();
    $('#caso').keyup(function(){
        table.column($(this).data('index')).search(this.value).draw();
    })
    $('#nombrecompleto').keyup(function(){
        table.column($(this).data('index')).search(this.value).draw();
    })
    $('#estado').click(function(){s
        table.column($(this).data('index')).search(this.value).draw();
    })
    $('#identificacion').keyup(function(){
        table.column($(this).data('index')).search(this.value).draw();
    })
})

