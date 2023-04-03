from logger.logger import setup_logger
from network.regressor import regressor
from tracker.tracker import tracker
from tracker.tracker_manager import tracker_manager

prototxt = 'model/tracker.prototxt'
model = 'model/tracker.caffemodel'
logger = setup_logger(logfile=None)

#inputVideoPath = 0 # for webcam
inputVideoPath = '/home/rgblab/DJI_0108_HD.MP4'
# inputVideoPath = 'Input/Trim840.mp4'

objRegressor = regressor(prototxt, model, logger)
objTracker = tracker(objRegressor)
objTrackerVis = tracker_manager(objRegressor, objTracker, logger)

# objTrackerVis.trackAll(inputVideoPath, save_tracking=False, show_tracking=True)
objTrackerVis.trackLive(0, show_tracking=True)
