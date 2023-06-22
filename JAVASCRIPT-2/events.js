
button = document.querySelector('.button');
contenedor1 = document.querySelector('.contenedor1');
contenedor2 = document.querySelector('.contenedor2');

//Event handlers
// button.onclick = () => {
//     alert('hola');
// };   asi no


//Events Listeners y el Event Flow
contenedor1.addEventListener( "click", (e) => { 
    alert('contenedor1');
} );

contenedor2.addEventListener( "click", (e) => { 
    alert('contenedor2');
    e.stopPropagation(); // event stop propagation
}, true );

button.addEventListener( "click", (e) => { 
    alert('button');
    console.log(e); // Event Object
} );

// las funciones flecha no funcionan POR FUERA con los event listeners

// Event Flow

// this explanation about Event Flow looks quite interesting 


//Capturing Phase: During the capturing phase, the event is triggered at the highest-level element in the DOM hierarchy and then propagates down to the target element. This means that the event is first handled by the outermost ancestor element and then moves inward towards the target element.

// Target Phase: Once the event reaches the target element, the event is triggered and handled at that specific element.

// Bubbling Phase: After the target phase, the event continues to propagate upward through the DOM hierarchy, triggering and handling the event on each ancestor element, starting from the target element and moving outward.



/* <div id="outer">
     <div id="middle">
       <div id="inner">Click me</div>
     </div>
   </div> */

// Capturing Phase: The event starts at the top-level element (in this case, the "outer" div) and propagates down the DOM hierarchy towards the target element ("inner" div).

// Target Phase: The event triggers and is handled at the target element ("inner" div).

// Bubbling Phase: The event continues to propagate upward through the DOM hierarchy, triggering and handling the event on each ancestor element (first "middle" div, then "outer" div).

