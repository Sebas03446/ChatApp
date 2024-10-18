<template>
    <div class="flex items-end space-x-2 w-1/2">
        <textarea
            id="input-chat"
            placeholder="Type a message..."
            class="flex-1 resize-none  bg-slate-900 text-white rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-indigo-600 min-h-10 overflow-x-hidden overflow-y-auto max-h-72"
            :value="modelValue"
            @input="handleInput($event)"
            @click.stop
            ref="textArea"
        ></textarea>
        <button
            class="h-10 w-10 rounded-full bg-indigo-600 text-white flex items-center justify-center hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-600"
            @click="handleClick"
        >
            <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                class="w-5 h-5"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M14 5l7 7m0 0l-7 7m7-7H3"
                />
            </svg>
        </button>
    </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

defineProps({
    modelValue: {
        type: String,
        required: true
    },

});

const emit = defineEmits(['update:modelValue'])

const handleInput = ($event) => {
    emit('update:modelValue', $event.target.value)
}


const handleClick = () => {
    emit('button-click');
};

</script>
