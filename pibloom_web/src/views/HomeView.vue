<script>
export default {
  data() {
    return {
      question: '',
      thinking: "I'm only a pie, let me think . . .                ",
      answer: '',
      api_result: ''
    }
  },

  watch: {
    // whenever question changes, this function will run
    question(newQuestion, oldQuestion) {
      if (newQuestion.includes('?')) {
        this.getAnswer()
      }
    }
  },

  methods: {
    async getAnswer() {
      let context = this;
      let thinking = this.thinking;

      let timer;
      let i = 0;

      function type() {
        // print the current charater with current index
        context.answer = thinking.substring(0, i);
        // increase the index
        i++;
        // if the index reaches the maximum text length, cease the timer
        if(i >= thinking.length) {
          clearInterval(timer);
          context.answer = context.api_result;
        }
      }

      // pass in function, instead of calling it
      timer = setInterval(type, 104);

      try {
        const res = await fetch('https://yesno.wtf/api')
        this.api_result = (await res.json()).answer
      } catch (error) {
        this.api_result = 'Error! Could not reach the API. ' + error
      }
    }
  }
}
</script>

<template>
  <div class="pibloom">
    <div class="question">
      <input v-model.lazy="question" placeholder="  ask me anything . . ." class="form"/>
    </div>
    <div class="answer green">
      <span>{{answer}}</span>
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

.question {
  border-bottom: 2px solid var(--color-border);
  border-radius: 10px;
  margin: 0 auto;
  width: 50%;
  min-width: 250px;
}

.form {
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