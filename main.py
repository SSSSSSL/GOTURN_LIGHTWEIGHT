from logger.logger import setup_logger
from network.regressor import regressor
from tracker.tracker import tracker
from tracker.tracker_manager import tracker_manager

#################################################################################
# RTX 3090
# [Show] Avg FPS 90
# [Save] Avg FPS 69
# [None] Avg FPS 118
# prototxt = 'model/tracker.prototxt'
# model = 'model/tracker.caffemodel'

#################################################################################
# RTX 3090
# [Show] Avg FPS 95
# [Save] Avg FPS 72
# [None] Avg FPS 120
# prototxt = 'model/myTracker.prototxt'
# model = 'myDump_model_iter_50000.caffemodel'

# prototxt = 'model/myTracker.prototxt'
# model = 'myDump_model_iter_100000.caffemodel'

# prototxt = 'model/myTracker.prototxt'
# model = 'myDump_model_iter_150000.caffemodel'

# prototxt = 'model/myTracker.prototxt'
# model = './backup/my2Dump_model_iter_50000.caffemodel'
#################################################################################
# RTX 3090
# prototxt = 'model/tiny/tinyTracker_deploy.prototxt'
# model = './backup/tinyDump_model_iter_40000.caffemodel'
#################################################################################
# RTX 3090
prototxt = 'model/tiny_v2/tiny2Tracker_deploy.prototxt'
model = './tiny2Dump_model_iter_5000.caffemodel'
#################################################################################

logger = setup_logger(logfile=None)

inputVideoPath = '/home/rgblab/Videos/드론촬영영상/test1.mp4'
# inputVideoPath = '/home/rgblab/Videos/드론촬영영상/crop2.mp4'

print('regressor')
objRegressor = regressor(prototxt, model, logger)
print('regressor done')

print('tracker')
objTracker = tracker(objRegressor)
print('tracker done')

print('tracker manager')
objTrackerVis = tracker_manager(objRegressor, objTracker, logger)
print('tracker manager done')

objTrackerVis.trackAll(inputVideoPath, save_tracking=False, show_tracking=True)
# objTrackerVis.trackLive(0, show_tracking=True)
# objTrackerVis.trackLive(4, show_tracking=True) # for intel real sense

