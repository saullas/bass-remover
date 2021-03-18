from pydub import AudioSegment
from pydub.playback import play
from pydub.scipy_effects import high_pass_filter

myAudioFile = AudioSegment.from_mp3("song.mp3")

# read in audio file and get the two mono tracks
sound_stereo = AudioSegment.from_file(myAudioFile, format="mp3")
sound_mono = sound_stereo.split_to_mono()
sound_monoL, sound_monoR = sound_mono[0], sound_mono[1]

# Invert phase of the Right audio file
sound_monoR_inv = sound_monoR.invert_phase()

# Merge two L and R_inv files, this cancels out the centers
# sound_CentersOut = sound_monoL.overlay(sound_monoR_inv)

filtered_stereo = high_pass_filter(sound_stereo, cutoff_freq=330)
finished = filtered_stereo + sound_monoL + sound_monoR_inv

# Export merged audio file
finished.export(out_f="finished", format="mp3")

play(finished)
