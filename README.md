## Demo
https://youtu.be/m6HQlJe1jvw?t=125

## DevPost
https://devpost.com/software/epilepsy-safe-viewer

## Inspiration
Over 50 million people suffer from epilepsy worldwide, making it one of the most common neurological diseases. With the rise in digital adoption, people who suffer from epilepsy are at risk from online videos that may trigger seizure responses. This can have adverse health effects on the lives of epileptic individuals and inhibits their interaction with technology. Often, there are warnings on videos that may trigger seizures, however, not much effort is made to resolve the problem. Our goal is clear, to provide a solution that proactively solves the problem and increases accessibility for this target group. 

## What it does
We built a chrome extension that interacts with YouTube videos and provides users with a warning in advance of seizure-inducing content and applies a filter to allow people to continue watching the video.

## How we built it
We first started off by building our flask server that has an open endpoint where the youtube video url is passed. This video is then downloaded to our server using PyTube and passed to openCv which determines the luminance values across the video. This dataset is then pre-processed and passed to the Azure Anomaly Detection model which determines anomalies in the luminance dataset. These anomalies represent portions in the youtube video where there are large discrepancies in light variation and hence, could trigger potential seizures for photosensitive epileptic users. The anomaly dataset is then processed to determine the timestamps in the video where these events occur. This dataset is then returned to a google chrome extension which overlays a dark filter over the video during these anomaly timestamps, thus preventing a potential seizure.

## Challenges we ran into
The first major challenge we faced was attempting to use Google Cloud Services as our anomaly detector for our luminance dataset as this service required us to package the data into a model and then create an anomaly detection model. As we were inexperienced in this subject, we were unable to complete this objective, this prevented us from using Google Cloud Services and caused us to lose precious development time. Another challenge that we faced was with the framerate of our downloaded videos. In our first iteration of creating the mvp, we were originally processing the youtube videos at a frame rate of 8 frames per second while creating the video timestamps on the anomaly data at a frame rate of 30 frames per second. This caused the extension to overlay the seizure warning filter at incorrect times of the video. Once we noticed that we were incorrectly downloading the videos at a slower frame rate, we were able to swiftly fix this issue.

## What's next for Epilepsy Safe Viewer
The first thing that we wanted to do as a team was some form of user testing on the product to determine the effectiveness of the product while also determining potential improvement areas. This would allow us to reiterate through our design process and make the product even better at solving our targeted user group???s problem. We also wanted to try applying our extension to users that face startle epilepsy by determining anomalies in the audio decibel levels of Youtube videos and normalizing the audio based on this. Lastly, we wanted to look into potential opportunities of expanding this product to other video platforms such as Netflix and TikTok, thus increasing the inclusivity and accessibility of this user group with technology.
