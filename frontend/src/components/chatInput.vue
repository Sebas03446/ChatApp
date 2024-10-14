<template>
    <div class="flex ">
        <textarea id="input-chat" placeholder="Type a message..."
            class="rounded-md border-gray-200 py-1 pe-3 ps-3 shadow-sm sm:text-sm overflow-auto resize-none field-sizing: content w-full"
            :value="modelValue" @input="handleInput($event)"></textarea>

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

</script>
