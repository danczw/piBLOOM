<script>
import axios from "axios";

export default {
  data() {
    return {
      prompt: "",
      thinking: "I'm just a pi, let me think . . .                ",
      answer: "",

      api_url: "http://127.0.0.1:5000/chat/", // TODO: move to env
      api_result: "",
    };
  },

  watch: {
    // whenever prompt changes, this function will run
    prompt(newPrompt, oldPrompt) {
      if (newPrompt !== oldPrompt) {
        this.getAnswer();
      }
    },
  },

  methods: {
    async getAnswer() {
      let context = this;
      let thinking = context.thinking;

      let timer;
      let i = 0;

      function type() {
        // print the current charater with current index
        context.answer = thinking.substring(0, i);
        // increase the index
        i++;
        // if the index reaches the maximum text length, cease the timer
        if (i >= thinking.length) {
          clearInterval(timer);
          context.answer = context.api_result;
        }
      }

      context.$refs.prompt_ref.value = "";
      // pass in function, instead of calling it
      timer = setInterval(type, 104);

      const headers = {
        "Content-Type": "application/json",
      };

      axios
        .post(
          context.api_url, // data POST url
          { content: context.prompt }, // data to be sent,
          { headers }
        )
        .then(function (response) {
          context.api_result = response.data.data;
          context.answer = context.api_result;
        })
        .catch(function (error) {
          context.api_result = "Error! Could not reach the API. " + error;
        });
    },
  },
};
</script>

<template>
  <div class="pibloom">
    <div class="prompt">
      <input
        ref="prompt_ref"
        v-model.lazy="prompt"
        placeholder="  give me a prompt . . ."
        class="input"
      />
    </div>
    <div class="answer green">
      <span>{{ answer }}</span>
    </div>
  </div>
</template>

<style scoped>
.pibloom {
  text-align: center;
  font-size: 1.2rem;
  padding-top: 2rem;
  display: flex;
  flex-direction: column;
  margin: 0 auto;
  width: 90%;
  min-width: 300px;
}

.prompt {
  border-bottom: 2px solid var(--color-border);
  border-radius: 10px;
  margin: 0 auto;
  width: 50%;
  min-width: 250px;
}

.input {
  width: 100%;
  border: 0;
  outline: 0;
  font-size: 1.2rem;
  padding: 0.5rem;
  border-radius: 10px;
  background-color: var(--color-background);
  color: var(--color-heading);
}

.answer {
  margin: 2rem auto 0 auto;
  padding-left: 1rem;
  width: 50%;
  min-width: 250px;
  text-align: left;
}
</style>
