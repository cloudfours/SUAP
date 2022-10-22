
const body = document.querySelector('#boy')
const menu = document.querySelector('#side')
const openbtn = document.querySelector('#boton')

openbtn.addEventListener('click',()=>{
    open_close_menu()
})
function open_close_menu(){
    body.classList.toggle('body_move')
    menu.classList.toggle('menu_side_move')
}
if(window.innerWidth<760){
    body.classList.add('body_move')
    menu.classList.add('menu_side_move')
}
window.addEventListener('resize',function (){
    if(window.innerWidth<760){
        body.classList.remove('body_move')
        menu.classList.remove('menu_side_move')
    }
     if(window.innerWidth<760){
        body.classList.add('body_move')
        menu.classList.add('menu_side_move')
    }
})

