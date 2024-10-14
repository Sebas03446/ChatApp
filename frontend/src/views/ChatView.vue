<script setup>
import { ref } from 'vue';
import ChatInput from '@/components/chatInput.vue';
import ChatButton from '@/components/chatButton.vue';

const inputValue = ref('');

const handleButtonClick = () => {
    console.log('Button clicked!');
};


</script>

<template>
    <div class="flex w-full h-full justify-center">
        <div class="fixed bottom-0 justify-center p-14 w-full">
            <div class="test flex justify-center space-x-2 max-h-64 w-full">
                <ChatInput v-model="inputValue" class="w-1/2"  />
                <ChatButton @click="handleButtonClick" class="max-h-12 self-end" />
            </div>
        </div>
    </div>
</template>


<style scoped></style>
