

### Report example
![Report plot](report.png)


After running the script with defualt settings you will get **./out** dir with debug frames images and **report.csv** file with format "time, vehicles".

## How to run script
```
pip install -r ../requirements.txt
```

Edit **traffic.py** if needed:
```
IMAGE_DIR = "./out"
VIDEO_SOURCE = "input.mp4"
SHAPE = (720, 1280)  # HxW
EXIT_PTS = np.array([
    [[732, 720], [732, 590], [1280, 500], [1280, 720]],
    [[0, 400], [645, 400], [645, 0], [0, 0]]
])

...

pipeline = PipelineRunner(pipeline=[
        ContourDetection(bg_subtractor=bg_subtractor,
                         save_image=True, image_dir=IMAGE_DIR),
        # we use y_weight == 2.0 because traffic are moving vertically on video
        # use x_weight == 2.0 for horizontal.
        VehicleCounter(exit_masks=[exit_mask], y_weight=2.0),
        Visualizer(image_dir=IMAGE_DIR),
        CsvWriter(path='./', name='report.csv')
    ], log_level=logging.DEBUG)
```
Run script:
```
python traffic.py
```

## How to create video from processed images
```
chmod a+x make_video.sh
./make_video.sh
```

## How to create report plot
```
python plot.py [path to the csv report] [number of seconds to group by] 
```

