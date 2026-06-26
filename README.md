# 🎡 La Ruleta de la Suerte — Desafíos de Ingeniería Visual y Arquitectura en Consola

```
 _____   _____   _____   _____   _____   _____   _____   _____  
│█████│ │     │ │     │ │     │ │     │ │     │ │     │ │█████│ 
│█████│ │  R  │ │  U  │ │  L  │ │  E  │ │  T  │ │  A  │ │█████│ 
│█████│ │     │ │     │ │     │ │     │ │     │ │     │ │█████│ 
 ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾  
 _____   _____   _____   _____   _____   _____   _____   _____  
│█████│ │     │ │     │ │█████│ │     │ │     │ │█████│ │█████│ 
│█████│ │  D  │ │  E  │ │█████│ │  L  │ │  A  │ │█████│ │█████│ 
│█████│ │     │ │     │ │█████│ │     │ │     │ │█████│ │█████│ 
 ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾  
 _____   _____   _____   _____   _____   _____   _____   _____  
│█████│ │     │ │     │ │     │ │     │ │     │ │     │ │█████│ 
│█████│ │  S  │ │  U  │ │  E  │ │  R  │ │  T  │ │  E  │ │█████│ 
│█████│ │     │ │     │ │     │ │     │ │     │ │     │ │█████│ 
 ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾   ‾‾‾‾‾ 
```
---
Este proyecto nace como una práctica para clase para aprender POO.

En lugar de limitarme a hacer un juego básico de adivinar texto plano en una línea, aproveché el proyecto para investigar un poco más por mi cuenta y añadirle varias funciones extras para ver hasta dónde podía exprimir la terminal.

---

* **El diseño del tablero por bloques:** No quería que las letras ocultas fuesen simples guiones bajo. Diseñé un sistema fiel al original visualmente donde cada letra se enmarca.

* **Control de líneas para frases largas (Word Wrapping):** El sistema divide automáticamente la frase en filas de máximo 14 casillas sin cortar ninguna palabra a la mitad, y luego formatea y centra todo verticalmente para que el panel se adapte solo (con un máximo de 4 filas, como en la televisión).

* **Lógicas especiales de la ruleta:** Implementar los puntos era lo fácil, así que quise replicar el comportamiento de los gajos: las quiebras, comodin, desbloquear todas las vocales...
 

---

## Organización del código

Para que el proyecto no fuese un único archivo gigante imposible de mantener, decidí estructurarlo separando las responsabilidades de cada parte:

* `controller/game.py`: Controla el motor principal, el bucle del juego, las comprobaciones de si un jugador tiene puntos para comprar vocales y cuándo se cambia de ronda.
* `models/panel.py`: Se encarga del estado de la frase oculta, de guardar las letras que ya se han probado y de fabricar los bloques tridimensionales para pintar el tablero.
* `models/register.py`: Funciona como un filtro para validar, limpiar y normalizar las frases nuevas que se añaden al juego.
* `models/scoreboard.py`: Lee el archivo JSON de las puntuaciones, las ordena y se encarga de calcular el tamaño de la tabla del ranking.
* `models/player.py` : Gestiona de forma independiente los marcadores de cada jugador (puntos de ronda vs totales) y las probabilidades de la ruleta.
* `view/vista.py` : Es la única parte que habla con el usuario. Utiliza secuencias ANSI para limpiar y refrescar las líneas de la terminal en tiempo real para que los menús se actualicen de forma limpia.
