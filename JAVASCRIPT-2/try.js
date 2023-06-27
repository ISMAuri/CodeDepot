dividirNumeros = (a, b) => {
    try {
      if (b === 0) {
        throw new Error("No se puede dividir por cero.");
      }
  
      let resultado = a / b;

      console.log("El resultado de la división es:", resultado);

    } catch (error) {
      console.error("Se produjo un error:", error.message);
    } finally {
      console.log("La función dividirNumeros ha finalizado.");
    }
  }

  dividirNumeros(10, 0); 
  