<script>
import axios from "axios";

export default {
  data() {
    return {
      disabled: 0,

      prompt: "",
      thinking: "I'm just a pi, let me think . . .                ",
      answer: "",

      server_url: import.meta.env.VITE_EXPRESS_URL || 'http://localhost:8080',
      api_result: "",
    };
  },

  methods: {
    async getAnswer() {
      let context = this;
      let thinking = context.thinking;

      let timer;
      let i = 0;

      // check if prompt is empty
      if (context.$refs.prompt_input_ref.value === "") {
        return;
      }

      context.disabled = 1;
      context.prompt = context.$refs.prompt_input_ref.value;
      context.$refs.prompt_button_ref.classList.add("button--loading");

      function typing_effect() {
        // print the current charater with current index
        context.answer = thinking.substring(0, i);
        // increase the index
        i++;
        // if the index reaches the maximum text length, cease the timer
        if (i >= thinking.length) {
          clearInterval(timer);
        }
      }

      // pass in function, instead of calling it
      timer = setInterval(typing_effect, 104);

      const headers = {
        "Content-Type": "application/json",
      };

      function api_response_reaction(this_context, func_timer, resp_string) {
        clearInterval(func_timer);
        this_context.api_result = resp_string;
        this_context.answer = this_context.api_result;
        this_context.$refs.prompt_input_ref.value = "";
        this_context.disabled = 0;
        this_context.$refs.prompt_button_ref.classList.remove("button--loading");
      }

      axios
        .post(
          context.server_url + '/chat/', // data POST url
          { content: context.prompt }, // data to be sent,
          { headers }
        )
        .then(function (response) {
          api_response_reaction(
            context,
            timer,
            response.data.data
          );
        })
        .catch(function (error) {
          api_response_reaction(
            context,
            timer,
            "Error! Could not reach the Middleware. " + error
          );
        });
    },
  },
};
</script>

<template>
  <div class="pibloom">
    <div class="prompt">
      <input
        class="input"
        ref="prompt_input_ref"
        :disabled="disabled == 1"
        @keyup.enter="getAnswer"
        placeholder="  give me a prompt . . ."
      />

      <button
        class="button"
        ref="prompt_button_ref"
        type="button"
        @click="getAnswer"
      >
        <span class="button__text">Go!</span>
      </button>
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
  display: flex;
  flex-direction: row;
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

.button {
  position: relative;
  padding: 8px 16px;
  background: hsla(160, 100%, 37%, 1);
  border: none;
  outline: none;
  border-radius: 2px;
  cursor: pointer;
}

.button:active {
  background: hsla(160, 100%, 37%, 1);
}

.button__text {
  font: bold 20px "Quicksand", san-serif;
  color: #ffffff;
  transition: all 0.2s;
}

.button--loading .button__text {
  visibility: hidden;
  opacity: 0;
}

.button--loading::after {
  content: "";
  position: absolute;
  width: 16px;
  height: 16px;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  border: 4px solid transparent;
  border-top-color: #ffffff;
  border-radius: 50%;
  animation: button-loading-spinner 1s ease infinite;
}

@keyframes button-loading-spinner {
  from {
    transform: rotate(0turn);
  }

  to {
    transform: rotate(1turn);
  }
}
</style>
