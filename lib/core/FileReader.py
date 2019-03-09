import librosa

class FileReader:
    def __init__(self):
        filename = librosa.util.example_audio_file()
        waveform, sampling_rate = librosa.load(filename)
        tempo, beat_frames = librosa.beat.beat_track(y=waveform, sr=sampling_rate)
        print('Estimated tempo beats per minute: ' + str(tempo))
        beat_times = librosa.frames_to_time(beat_frames, sr=sampling_rate)
        print('Saving to csv')
        librosa.output.times_csv('times.csv', beat_times)
