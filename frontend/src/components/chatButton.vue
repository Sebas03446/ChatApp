<template>
    <a
        class="inline-block rounded border border-indigo-600 p-3 text-indigo-600 hover:bg-indigo-600 hover:text-white focus:outline-none focus:ring active:bg-indigo-500"
        href="#"
        @click.prevent="handleClick"
    >
        <span class="sr-only"> Download </span>

        <svg
            class="size-5 rtl:rotate-180"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
        >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M14 5l7 7m0 0l-7 7m7-7H3"
            />
        </svg>
    </a>
</template>

<script setup>
import { defineEmits } from 'vue';

const emit = defineEmits(['click']);

const handleClick = () => {
    emit('click');
};
</script>
