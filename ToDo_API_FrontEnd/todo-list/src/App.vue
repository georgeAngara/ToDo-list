<template>
<div class="app-container">
  <h1>Lista de tareas</h1>
  <div class="task-input">
    <label for="tittle">Titulo:</label>
    <input type="text" placeholder="Titulo" v-model="title">
    <label for="description">Descripción:</label>
    <input type="text" placeholder="Descripción" v-model="description">
    <label for="priority">Prioridad:</label>
    <select v-model="priority" id="priority">
      <option disabled value="">Selecciona una prioridad</option>
      <option value="alto">Alto</option>
      <option value="medio">Medio</option>
      <option value="bajo">Bajo</option>
    </select>
    <button @click="addtask">Agregar</button>
  </div>
</div>
<div class="filters">
  <label >
    <input type="radio" value="all" v-model="filter">Todas
  </label>
  <label >
    <input type="radio" value="pending" v-model="filter">Pendientes
  </label>
  <label >
    <input type="radio" value="completed" v-model="filter">completadas
  </label>
  
</div>
<ul class="task-list">
  <li v-for="(task, index) in filteredTasks" 
  :key="task.id" 
  class="{completed:task.completed}"
  >
    <div class="view-mode" v-if="!task.editing">
      <input type="checkbox" v-model="task.completed" @change="editTaskCompleted(task)" >
      <span @dblclick="editTask(task)">{{ task.title }}</span>
      <span @dblclick="editTask(task)">{{ task.description }}</span>
      <span @dblclick="editTask(task)">{{ task.priority }}</span>
      <button @click="deleteTask(index)">Eliminar</button>
    </div>
    <div class="edit-mode" v-else>
      <!-- <input v-model="task.text" @keyup.enter="doneEditing(task)"> -->
      <input v-model="task.title" >
      <input v-model="task.description" >
      <select v-model="task.priority" id="priority" >
        <option disabled value="" >Selecciona una prioridad</option>
        <option value="Alto">Alto</option>
        <option value="Medio">Medio</option>
        <option value="Bajo">Bajo</option>
      </select>
      <button @click="doneEditing(task)">Editar</button>
      <button @click="cancelEditing(task)">cancelar</button>
    </div>      
  </li>    
</ul>

</template>
<script src="./app.js"></script>
<style scoped src="./app.css"></style>