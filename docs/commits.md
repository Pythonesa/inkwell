# 📖 Convenciones de Commits

Los mensajes de commits debe seguir la siguiente estructura:

`<gitmoji> tipo(scope): descripción breve`

Donde:

- `<gitmoji>`: Es un emoji que representa el propósito principal del commit. Para seleccionar el adecuado, consulta [Gitmoji](https://gitmoji.dev/).

- `tipo`: Indica el tipo de cambio que se ha realizado. Algunas opciones son:
  - `feat`: Introducción de nuevas características.
  - `fix`: Correcciones de errores.
  - `docs`: Cambios en la documentación.
  - `style`: Cambios que no afectan el significado del código (blancos, formato, etc).
  - `refactor`: Cambios en el código que no corrigen errores ni introducen características.
  - `test`: Adición o correcciones en tests.

- `scope`: (Opcional) Especifica qué parte del proyecto se ve afectada. Por ejemplo: `frontend`, `backend`, `database`, etc.

- `descripción breve`: Un breve resumen de los cambios realizados.
