<script setup>
import { ref } from 'vue';
import PromptContainer from '@/components/promptContainer.vue';

const inputValue = ref('');

const handleButtonClick = () => {
    console.log('Button clicked!');
};


const messages = ref([
    {
        id: 1,
        user
        : 'John Doe',
        text: 'Hello, how can I help you today?'
    },
    {
        id: 2,
        user: 'Jane Doe',
        text: 'I need help with my order.'
    },
    {
        id: 3,
        user: 'John Doe',
        text: 'Sure, what seems to be the problem?'
    },
]);

</script>

<template>
    <div class="flex w-full h-full">
        <div class="relative flex h-full w-1/4 hidden">
        </div>
        <div class="relative flex flex-col h-full w-full">
            <div class="bg-white w-full h-full overflow-y-auto">
                <div class="p-4">
                    <div v-for="message in messages" :key="message.id" class="mb-4">
                        <div class="font-bold">{{ message.user }}</div>
                        <div>{{ message.text }}</div>
                    </div>
                </div>
            </div>
            <div class="flex mt-auto w-full h-80 justify-center align-middle p-10">
                <PromptContainer v-model:modelValue="inputValue" @button-click="handleButtonClick" />
            </div>
            
        </div>
    </div>
</template>
