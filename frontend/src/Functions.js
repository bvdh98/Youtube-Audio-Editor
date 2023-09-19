export const loadVideo = async () => {
    try {
      const video = await import('./assets/video/final.mp4');
      return video.default;
    } catch (error) {
      console.error('Video not yet created', error);
      return null;
    }
  };