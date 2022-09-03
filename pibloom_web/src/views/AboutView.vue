<template>
  <div class="about">
    <div>Raspberry Pi cluster based BLOOM model serving.</div>
    <br />
    <div>
      Find out more on
      <a href="https://github.com/danczw/piBLOOM"
        >GitHub</a
      >
    </div>
    <div class="powerby">
      <div>Powered by:</div>

      <br />

      <div class="logos">
        <a href="https://bigscience.huggingface.co">
          <img
            alt="Bloom logo"
            class="logo"
            src="@/assets/bloom.png"
            height="125"
          />
        </a>
        <a href="https://www.raspberrypi.com">
          <img
            alt="Raspberry Pi logo"
            class="logo"
            src="@/assets/raspberrypi.svg"
            height="125"
          />
        </a>
      </div>
    </div>
  </div>
</template>

<style>
.about {
  text-align: center;
  font-size: 1.2rem;
  padding-top: 2rem;
  display: flex;
  flex-direction: column;
}

.powerby {
  padding-top: 20%;
  display: flex;
  flex-direction: column;
}

.logos {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

img {
  width: 300px;
}

/* @media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
} */
</style>
