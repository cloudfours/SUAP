$(document).ready(function () {
    let table =$('#example').DataTable({'bFilter':false,'language': espanol})
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
const espanol = {
    
        "autoFill": {
            "cancel": "Cancelar"
        },
        "buttons": {
            "collection": "Coleccion",
            "colvis": "Columna Visible",
            "colvisRestore": "Restaurar Columnas Visibles",
            "copy": "Copiar",
            "copyKeys": "presiones inicio + c para copiar ka infrocion de la tabla.  click en este mensaje para salir o esc.",
            "copySuccess": {
                "_": "Copiado con exito",
                "1": "Fila copiada con exito"
            },
            "copyTitle": "Tabla Copiada",
            "createState": "Crear estado",
            "pageLength": {
                "_": "ver %d filas",
                "-1": "Ver todas las Filas",
                "1": "Ver solo una fila"
            },
            "print": "Impresion",
            "removeAllStates": "Remover todos los estados",
            "removeState": "Remover",
            "renameState": "Renombrar",
            "savedStates": "Guardar Estado",
            "stateRestore": "Restaurar %d",
            "updateState": "Actualizar",
            "csv": "CSV",
            "excel": "Excel",
            "pdf": "PDF"
        },
        "datetime": {
            "hours": "hora",
            "minutes": "minuto",
            "months": {
                "0": "Enero",
                "1": "Febrero",
                "10": "Noviembre",
                "11": "Diciembre",
                "2": "Marzo",
                "3": "Abril",
                "4": "Mayo",
                "5": "Junio",
                "6": "Julio",
                "7": "Agosto",
                "8": "Septiembre",
                "9": "Octubre"
            },
            "next": "siguiente",
            "previous": "anterior",
            "seconds": "segundo",
            "weekdays": [
                "Dom",
                "Lun",
                "Mar",
                "Mir",
                "Jue",
                "Vie",
                "sab"
            ],
            "unknown": "desconocido",
            "amPm": [
                "am",
                "pm"
            ]
        },
        "editor": {
            "close": "Cerrar",
            "create": {
                "button": "Nuevo",
                "submit": "Crear",
                "title": "Crerar nueva entrada"
            },
            "edit": {
                "button": "Editar",
                "submit": "Actualizar",
                "title": "Editar Registro"
            },
            "error": {
                "system": "a ocurrido un error "
            },
            "multi": {
                "restore": "revertir cambios",
                "info": "Los elementos seleccionados contienen diferentes valores para esta entrada. Para editar y configurar todos los elementos de esta entrada en el mismo valor, haga clic o toque aquí, de lo contrario, conservar sus valores individuales.",
                "noMulti": "Múltiples valores"
            },
            "remove": {
                "button": "Borrar",
                "confirm": {
                    "_": "esta seguro de eliminar %d los registros",
                    "1": "esta seguro de eliminar el registro"
                },
                "submit": "Borrar",
                "title": "Borrar"
            }
        },
        "emptyTable": "Tabla Vacia",
        "info": "informacion",
        "infoEmpty": "Sin informacion",
        "lengthMenu": "Entradas",
        "loadingRecords": "Cargando...",
        "paginate": {
            "first": "primero",
            "last": "ultimo",
            "next": "siguiente",
            "previous": "anterior"
        },
        "processing": "Procesando",
        "search": "Busqueda",
        "searchBuilder": {
            "add": "agragar condicion",
            "button": {
                "_": "Creador de búsquedas (%d)",
                "0": "Creador de búsquedas"
            },
            "clearAll": "Quitar filtro",
            "condition": "Condicion",
            "data": "Datos",
            "deleteTitle": "eliminar regla",
            "logicAnd": "Y",
            "logicOr": "O",
            "value": "Valor"
        },
        "searchPanes": {
            "clearMessage": "Borrar Filtro",
            "collapseMessage": "desplegar todo",
            "emptyPanes": "No hay informacion",
            "loadMessage": "Cargando informacion",
            "showMessage": "Mostrar todos",
            "title": "Filtros Activos - %d"
        },
        "searchPlaceholder": "Busqueda en tabla",
        "select": {
            "cells": {
                "_": "%d celdas seleccionadas",
                "1": "1 celda seleccionada"
            },
            "columns": {
                "_": "%d columnas seleccionadas",
                "1": "1 columna seleccionada"
            }
        },
        "zeroRecords": "No se encontro informacion"
    
}