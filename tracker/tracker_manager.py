# Date: Wednesday 07 June 2017 11:28:11 AM IST
# Email: nrupatunga@whodat.com
# Name: Nrupatunga
# Description: tracker manager

import time
import cv2

from helper.BoundingBox import BoundingBox

opencv_version = cv2.__version__.split('.')[0]

class tracker_manager:

    """Docstring for tracker_manager. """

    def __init__(self, regressor, tracker, logger):
        """This is
        :regressor: regressor object
        :tracker: tracker object
        :logger: logger object
        :returns: list of video sub directories
        """
        self.regressor = regressor
        self.tracker = tracker
        self.logger = logger


    def trackAll(self, inputVideo, save_tracking=False, show_tracking=True):
        """Track the objects in the video
        """
        objRegressor = self.regressor
        objTracker = self.tracker

        vid = cv2.VideoCapture(inputVideo)

        ok, frame_0 =vid.read()
        if not ok:
            print('Couldnt read first frame')
            exit()

        if save_tracking:
            movie_number =0
            tracker_type ='GoturnGPU'
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
            FPS = vid.get(cv2.CAP_PROP_FPS)
            output_video_name = 'output_videos/movie_' + str(movie_number) + time.strftime(
                "_%d%m%Y_%H%M%S") + '_' + tracker_type + '.mp4'
            print(output_video_name)
            outVideo = cv2.VideoWriter(output_video_name, fourcc, int(FPS), (width, height))

        box_0 = cv2.selectROI(frame_0)
        cv2.destroyAllWindows()
        num_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

        #num_frames = 10000

        bbox_0 = BoundingBox(x1=box_0[0], y1=box_0[1], x2=box_0[0] +box_0[2], y2=box_0[1] +box_0[3])
        objTracker.init(frame_0, bbox_0, objRegressor)
        
        timerI = cv2.getTickCount()
        for i in range(1, num_frames-1):
            # vid.set(1,i)
            print('Tracking on frame:'+str(i)+'/'+str(num_frames))
            ok,frame = vid.read()
            if not ok:
                break
            ### Start timer
            timer = cv2.getTickCount()

            ### Update Tracker
            bbox = objTracker.track(frame, objRegressor)

            ### Print BBox
            # bbox.print_bb()

            ### Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

            ### Draw bounding box
            ImageDraw = frame.copy()
            #print('BBOX : ', bbox.x1, bbox.y1, bbox.x2, bbox.y2)
            ImageDraw = cv2.rectangle(ImageDraw, (int(bbox.x1), int(bbox.y1)), (int(bbox.x2), int(bbox.y2)), (255, 0, 0), 2)


            # Display FPS on frame
            cv2.putText(ImageDraw, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

            if show_tracking:
                cv2.imshow('Results', ImageDraw)
                cv2.waitKey(1)
            if save_tracking:
                outVideo.write(ImageDraw)
        timerF = cv2.getTickCount()
        Time_proc = (timerF-timerI)/cv2.getTickFrequency()
        print('Total processing time ='+ str(int(Time_proc))+'sec')
        print('Average FPS ='+ str(i / Time_proc))
        vid.release()
        if save_tracking:
                outVideo.release()


    def trackLive(self, videoIdx, show_tracking=True):
        """Track the objects in the video
        """
        objRegressor = self.regressor
        objTracker = self.tracker

        vid = cv2.VideoCapture(videoIdx, cv2.CAP_V4L2)
        vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        ok, frame_0 = vid.read()
        if not ok:
            print('Couldnt read first frame')
            exit()

        box_0 = cv2.selectROI(frame_0)
        cv2.destroyAllWindows()

        bbox_0 = BoundingBox(x1=box_0[0], y1=box_0[1], x2=box_0[0] +box_0[2], y2=box_0[1] +box_0[3])
        objTracker.init(frame_0, bbox_0, objRegressor)
        
        timerI = cv2.getTickCount()
        i = 0
        while True:
            print('Tracking on frame:'+str(i))
            ok,frame = vid.read()
            if not ok:
                break
            ### Start timer
            timer = cv2.getTickCount()

            ### Update Tracker
            bbox = objTracker.track(frame, objRegressor)

            ### Print BBox
            # bbox.print_bb()

            ### Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

            ### Draw bounding box
            ImageDraw = frame.copy()
            #print('BBOX : ', bbox.x1, bbox.y1, bbox.x2, bbox.y2)
            ImageDraw = cv2.rectangle(ImageDraw, (int(bbox.x1), int(bbox.y1)), (int(bbox.x2), int(bbox.y2)), (255, 0, 0), 2)

            # Display FPS on frame
            cv2.putText(ImageDraw, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

            if show_tracking:
                cv2.imshow('Results', ImageDraw)
                cv2.waitKey(1)
            i = i+1            
        timerF = cv2.getTickCount()
        Time_proc = (timerF-timerI)/cv2.getTickFrequency()
        print('Total processing time ='+ str(int(Time_proc))+'sec')
        print('Average FPS ='+ str(i / Time_proc))
        vid.release()


    def trackVot(self, videos, start_video_num, pause_val):
        """Track the objects in the video
        """
        objRegressor = self.regressor
        objTracker = self.tracker

        video_keys = list(videos.keys())
        for i in range(start_video_num, len(videos)):
            video_frames = videos[video_keys[i]][0]
            annot_frames = videos[video_keys[i]][1]

            num_frames = min(len(video_frames), len(annot_frames))

            # Get the first frame of this video with the intial ground-truth bounding box
            frame_0 = video_frames[0]
            bbox_0 = annot_frames[0]
            sMatImage = cv2.imread(frame_0)
            objTracker.init(sMatImage, bbox_0, objRegressor)
            for i in range(1, num_frames):
                frame = video_frames[i]
                sMatImage = cv2.imread(frame)
                sMatImageDraw = sMatImage.copy()
                bbox = annot_frames[i]
                
                if opencv_version == '2':
                    cv2.rectangle(sMatImageDraw, (int(bbox.x1), int(bbox.y1)), (int(bbox.x2), int(bbox.y2)), (255, 255, 255), 2)
                else:
                    sMatImageDraw = cv2.rectangle(sMatImageDraw, (int(bbox.x1), int(bbox.y1)), (int(bbox.x2), int(bbox.y2)), (255, 255, 255), 2)

                bbox = objTracker.track(sMatImage, objRegressor)
                if opencv_version == '2':
                    cv2.rectangle(sMatImageDraw, (int(bbox.x1), int(bbox.y1)), (int(bbox.x2), int(bbox.y2)), (255, 0, 0), 2)
                else:
                    sMatImageDraw = cv2.rectangle(sMatImageDraw, (int(bbox.x1), int(bbox.y1)), (int(bbox.x2), int(bbox.y2)), (255, 0, 0), 2)

                cv2.imshow('Results', sMatImageDraw)
                cv2.waitKey(10)