const boton = document.getElementById('enviar');
const tabla = document.getElementById('Datos');

boton.addEventListener('click',(e)=>{
    e.preventDefault();

    const formulario = document.getElementById('formulario');
        const nombre = document.getElementById('nombre');
        const rut = document.getElementById('Rut');
        const tipo = document.getElementById('Tipo');
        const Medico = document.getElementById('Medico');
        
        if (nombre.value.length !== 0 && rut.value.length !== 0 && tipo.value.length !==0 && Medico.value.length !==0 ){
            boton.classList.remove('disabled');
            const datos = {nombre:nombre.value,rut:rut.value,tipo:tipo.value,medico:Medico.value}
            AgregarDatos(datos);
            formulario.reset();
        }
})

function AgregarDatos(datos){
    let Items  = []
    let DataStorage = localStorage.getItem('datos');
   if(DataStorage !== null){
       Items = JSON.parse(DataStorage);
   }
   Items.push(datos);
   localStorage.setItem('datos',JSON.stringify(Items));
   mostrardatos();
}

function mostrardatos(){
    const datos = JSON.parse(localStorage.getItem('datos'));
    const items = datos.map((item,index) => {
        return `
        <tr>
            <th scope="row">${index +1 }</th>
            <td>${item.nombre}</td>
            <td>${item.rut}</td>
            <td>${item.tipo}</td>
            <td>${item.medico}</td>
         </tr>

        `
    })
    tabla.innerHTML = items.join('');
}

document.addEventListener("DOMContentLoaded", function () {
   mostrardatos();

});