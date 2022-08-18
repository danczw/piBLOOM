from transformers import BloomForCausalLM, BloomTokenizerFast, TextGenerationPipeline

class bloom_model:
    def __init__(self):
        self.tokenizer = BloomTokenizerFast.from_pretrained(
            pretrained_model_name_or_path = './model/'
            , local_files_only = True
            , low_cpu_mem_usage = True
        )
        
        self.model = BloomForCausalLM.from_pretrained(
            pretrained_model_name_or_path = './model/'
        )
        
        self.generator = TextGenerationPipeline(
            task = 'text-generation',
            model = self.model,
            tokenizer = self.tokenizer
        )
                        
    def predict(self, content: str) -> str:
        answer = self.generator(content, max_new_tokens=100)
        return answer
