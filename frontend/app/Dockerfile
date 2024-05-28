# Usar una imagen base de Node.js para construir la aplicación
FROM node:14

# Crear y establecer el directorio de trabajo
WORKDIR /app

# Copiar el package.json y package-lock.json
COPY package*.json ./

# Instalar las dependencias
RUN npm install

# Copiar el resto de los archivos de la aplicación
COPY . .

# Exponer el puerto 3000
EXPOSE 3000

# Iniciar la aplicación
CMD ["npm", "start"]
