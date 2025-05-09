import api from './services/api.js';

export default{
    name:'App',
    data(){
        return {
            title: '',
            priority: '',
            description: '',
            tasks:this.fetchTasks(),
            filter:'all'
        }
    },
    computed: {
        filteredTasks() {        
            if (this.filter === 'pending') {
                return this.tasks.filter(t => !t.completed);
            } else if (this.filter === 'completed') {
                return this.tasks.filter(t => t.completed);
            } else {
                return this.tasks;
            }
        }
    },
    methods: {
        async fetchTasks() {
            try {
                const response = await api.get('/tasks');
                this.tasks = response.data;
            } catch (error) {
                console.error('Error al obtener tareas:', error);
            }
        },
        async addtask(){
            const title = this.title.trim();
            const priority = this.priority.trim();
            const description = this.description.trim();

            if (title != '') {
                const newTask = {
                    title: title,
                    priority: priority,
                    description: description,
                    completed: false
                };

                try{
                    const response = await api.post('/tasks', newTask, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });

                    console.log(response)
                    console.log('Tarea creada:', response.data);
                    this.fetchTasks(); // Recarga las tareas

                    this.title='';
                    this.priority='';
                    this.description='';

                } catch (error) {
                    console.error('Error al agregar tarea:', error);
                }
                

                
            }
        },
        async editTaskCompleted(task){
            
            try {
                await api.put('/task/'+task.id, task);
                console.log("Tarea actualizada");
                console.log(this.tasks)
                task.editing=false;
            } catch (error) {
                console.error('Error al actualizar tarea:', error);
            }
        },
        editTask(task){
            task.editing=true;
        },
        async doneEditing(task){
            task.title = task.title.trim();
            task.priority = task.priority.trim();
            task.description = task.description.trim();
            if(!task.title){
                this.deleteTask(this.tasks.indexOf(task))
            }else{                
                try {
                    console.log('task.id **',task.id)
                    await api.put('/task/'+task.id, task);
                    console.log("Tarea actualizada");
                    console.log(this.tasks)
                    task.editing=false;
                } catch (error) {
                    console.error('Error al actualizar tarea:', error);
                }

            }
        },
        cancelEditing(task){
            task.editing=false;
        },
        async deleteTask(index){
            const task = this.tasks[index];
            try {
                await api.delete('tasks/'+task.id);
                this.tasks.splice(index, 1);
            } catch (error) {
                console.error("Error al eliminar tarea:", error);
            } 
        },
        async mounted() {
            this.fetchTasks();
        }
    }        
}