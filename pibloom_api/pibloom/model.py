from distutils.command.config import config
from transformers import AutoConfig, BloomForCausalLM, BloomTokenizerFast, TextGenerationPipeline

class bloom_model:
    def __init__(self, path: str = './model/'):
        # local model files paths
        self.model_path = path
        
        # load BLOOM config from local files
        self.config = AutoConfig.from_pretrained(
            pretrained_model_name_or_path = self.model_path + 'config.json'
        )
        
        #  load BLOOM tokenizer from local files
        self.tokenizer = BloomTokenizerFast.from_pretrained(
            pretrained_model_name_or_path = self.model_path
            , local_files_only = True
            # , low_cpu_mem_usage = True
        )
        
        # load BLOOM model from local files
        self.model = BloomForCausalLM.from_pretrained(
            pretrained_model_name_or_path = self.model_path
            , config = self.config
            , local_files_only = True
            # , low_cpu_mem_usage = True
        )
        
        # define pipeline for inference
        self.generator = TextGenerationPipeline(
            task = 'text-generation'
            , model = self.model
            , tokenizer = self.tokenizer
        )
    
    def predict(self, content: str) -> str:
        inputs = self.tokenizer(content, return_tensors='pt')
        output = self.tokenizer.decode(
            self.model.generate(
                inputs["input_ids"]
                , do_sample = True
                , top_k = 50
                , top_p = 0.9
                , max_length = 100
            )[0]
        )
        
        return output
