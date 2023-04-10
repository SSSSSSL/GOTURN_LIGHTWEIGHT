IMAGENET_FOLDER='/home/rgblab/tracking/dataset/ILSVRC2014/'
ALOV_FOLDER='/home/rgblab/tracking/dataset/ALOV/'

# INIT_CAFFEMODEL='./model/tracker.caffemodel'
# INIT_CAFFEMODEL='./model/tracker_init.caffemodel'
INIT_CAFFEMODEL='./myDump_model_iter_50000.caffemodel'


# TRACKER_PROTO='./model/tracker.prototxt'
# TRACKER_PROTO='./model/myTracker.prototxt'
# TRACKER_PROTO='./model/mobile/mobileTracker_train.prototxt'
# TRACKER_PROTO='./model/tiny/tinyTracker_train.prototxt'
# TRACKER_PROTO='./model/tiny_v2/tiny2Tracker_train.prototxt'
TRACKER_PROTO='./model/tiny_v3/tiny3Tracker_train.prototxt'


# SOLVER_PROTO='./model/solver.prototxt'
# SOLVER_PROTO='./model/mySolver.prototxt'
# SOLVER_PROTO='./model/mobile/mobileSolver.prototxt'
# SOLVER_PROTO='./model/tiny/tinySolver.prototxt'
# SOLVER_PROTO='./model/tiny_v2/tiny2Solver.prototxt'
SOLVER_PROTO='./model/tiny_v3/tiny3Solver.prototxt'


python3 -m train.train \
--imagenet $IMAGENET_FOLDER \
--alov $ALOV_FOLDER \
--init_caffemodel $INIT_CAFFEMODEL \
--train_prototxt $TRACKER_PROTO \
--solver_prototxt $SOLVER_PROTO \
--lamda_shift 5 \
--lamda_scale 15 \
--min_scale -0.4 \
--max_scale 0.4 \
--gpu_id 0