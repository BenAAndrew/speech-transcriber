from subprocess import check_output

TARGET_BITRATE = "128"


def convert_audio(input_path: str, output_path: str):
    check_output(
        [
            "ffmpeg",
            "-i",
            input_path,
            "-ac",
            "1",
            "-ab",
            TARGET_BITRATE,
            "-acodec",
            "pcm_s16le",
            output_path,
        ]
    )
