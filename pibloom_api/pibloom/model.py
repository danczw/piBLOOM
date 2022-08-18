from transformers import BloomModel, BloomTokenizerFast, pipeline

class bloom_model:
    def __init__(self):
        self.tokenizer = BloomTokenizerFast.from_pretrained(
            "bigscience/bloom-560m"
            , low_cpu_mem_usage=True
        )
        
        self.model = BloomModel.from_pretrained("bigscience/bloom-560m")
        
        # self.generator = pipeline(
        #     "text-generation"
        #     , model=self.model
        #     , tokenizer=self.tokenizer
        # )
        
        self.generator = pipeline(
            model="bigscience/bloom-560m"
            , tokenizer=self.tokenizer
        )
        
    def predict(self, content: str) -> str:
        answer = self.generator(content, max_new_tokens=100)
        return answer