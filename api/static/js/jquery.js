$(document).ready(function () {
    let table = $('#example').DataTable({
        "language": {
            "url": "//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json"
        },
        responsive: true,
      
    })
 
    new $.fn.dataTable.FixedHeader( table );
    $('#example').DataTable();
    $('#caso').keyup(function () {
        table.column($(this).data('index')).search(this.value).draw();
    })
    $('#nombrecompleto').keyup(function () {
        table.column($(this).data('index')).search(this.value).draw();
    })
    $('#estado').click(function () {
        table.column($(this).data('index')).search(this.value).draw();
    })
    $('#identificacion').keyup(function () {
        table.column($(this).data('index')).search(this.value).draw();
    })



})
const acces = document.getElementById('acces')
const cabecera = document.getElementById('cabecera')
const icons = document.querySelector('#boton')
const menus = document.getElementById('side')
const user = document.getElementById('user')
const i = document.querySelectorAll('i')
const menu_user = document.getElementById('menu_user')
const allicons=document.querySelectorAll('a')
const titulo = document.getElementById('titulo')
const encabezadotabla = document.querySelectorAll('thead')
const letraenca=document.querySelectorAll('th')
acces.addEventListener('click', agregar)

function agregar() {
    cabecera.classList.toggle('accesibilidad_color')
    menus.classList.toggle('accesibilidad_color')
    
    user.classList.toggle("text-dark")
    menu_user.classList.toggle("text-dark")
    i.forEach(x=>x.classList.toggle('text-dark'))
    allicons.forEach(element => {
        element.classList.toggle('text-dark')
    });
    titulo.classList.toggle("text-dark")
    encabezadotabla.forEach(e=>{
        if(  e.classList.contains('bg-primary','bg-gradient')){
              e.classList.remove('bg-primary','bg-gradient')
              e.classList.toggle('accesibilidad_color')
        }else{
        e.classList.remove('accesibilidad_color')
        e.classList.add('bg-primary','bg-gradient')
      
        }
    })
    letraenca.forEach(x=>{
        x.classList.toggle('text-dark')
    })

}
