import azure.cognitiveservices.speech as speechsdk
import os
import numpy as np

# Timeline Function
class Time_line:
    time_line  = []
    run_wait_ratio = 0.8
    
    def save_value(self,time):
        self.time_line.append(time)
        
    def set_run_wait_ratio(self,ratio):
        self.run_wait_ratio = ratio
    
    # All time number was rounded to 3rd decimal place.
    def get_time_line(self):
        return self.time_line
    
    def get_interval_time(self):
        self.interval_time = []
        for number in range(len(self.time_line)-1):
            interval = self.time_line[number+1]-self.time_line[number]
            self.interval_time.append(np.round(interval,3))
            
        return self.interval_time
    
    def get_run_time(self):
        run_ratio = self.run_wait_ratio
        self.run_time = list(map((lambda t: np.round(t*run_ratio,3)), self.interval_time))
        
        return self.run_time
    
    def get_wait_time(self):
        wait_ratio = 1-self.run_wait_ratio
        self.wait_time = list(map((lambda t: np.round(t*(wait_ratio),3)), self.interval_time))
        return self.wait_time  
    
class voice_tools():
    voice_time = Time_line()
    
    def voice_generate(self,text_name):
        # Authorization code
        KEY = "4bb0505e82014aabbe7fb337d143eacf"
        
        # Set file path. 
        path = ""
        text_path = os.path.join(path,text_name)
        voice_path = os.path.join(path,'voice_output.mp3')
        
        # Authorization & Setting
        speech_config = speechsdk.SpeechConfig(subscription=KEY, region="eastasia") # authorization
        audio_config = speechsdk.audio.AudioOutputConfig(filename=voice_path) # set voice output path
        speech_config.speech_synthesis_voice_name = 'zh-TW-YunJheNeural'    # set language
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,
                                                        audio_config=audio_config)
        
        # Get time line
        speech_synthesizer.bookmark_reached.connect(
            lambda evt: self.voice_time.save_value(evt.audio_offset/10000000))
        
        self.voice_time.get_interval_time()
        self.voice_time.get_run_time()
        self.voice_time.get_wait_time()
        
        # Speech synthesis
        with open(text_path, 'r', encoding="utf-8") as f:
            text = f.read()
        speech_synthesis_result = speech_synthesizer.speak_ssml_async(text).get()
        
if __name__ == '__main__':
    a = voice_tools()
    a.voice_generate('text_output.txt')
    time_line = a.voice_time.get_time_line()
    a.voice_time.set_run_wait_ratio(1)
    interval_time = a.voice_time.get_interval_time()
    run_time = a.voice_time.get_run_time()
    wait_time = a.voice_time.get_wait_time()
    print(time_line)
    print(interval_time)