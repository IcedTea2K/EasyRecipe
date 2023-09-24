package com.easy_recipe.front_end
//
//import android.os.Bundle
//import android.util.Log
//import androidx.activity.ComponentActivity
//import androidx.activity.compose.setContent
//import androidx.compose.material3.Text
//import androidx.compose.runtime.Composable
//import androidx.compose.ui.Modifier
//import androidx.camera.core.Preview
//
//
//class CaptureViewLame : ComponentActivity() {
////    private lateinit var viewBinding: ActivityMainBinding
////    private lateinit var cameraExecutor: ExecutorService
////    private var imageCapture: ImageCapture? = null
////    private val requestPermissionLauncher = registerForActivityResult(
////        ActivityResultContracts.RequestPermission()
////    ) { isGranted: Boolean ->
////        if (isGranted) {
////            Log.i("Main", "Permission Granted")
////        } else {
////            Log.i("Main", "Permission Denied")
////        }
////    }
//    override fun onCreate(savedInstanceState: Bundle?) {
//        super.onCreate(savedInstanceState)
//        Log.i("CaptureView", "Helloooooooooo")
//        setContent{
//            Camera()
//        }
////        requestCameraPermission()
//    }
////
////    /**
////     * Start the camera and show the preview
////     */
////    private fun startCamera() {
////        val cameraProviderFuture = ProcessCameraProvider.getInstance(this)
////        cameraProviderFuture.addListener({
////            val cameraProvider: ProcessCameraProvider = cameraProviderFuture.get()
////            val preview = Preview.Builder()
////                .build()
////                .also {
////                    it.setSurfaceProvider(viewBinding.viewFinder.surfaceProvider)
////                }
////            val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA
////
////            try {
////                cameraProvider.unbindAll()
////                cameraProvider.bindToLifecycle(this, cameraSelector, preview)
////            } catch (exec: Exception) {
////                Log.e("CaptureView", "Use case binding failed", exec)
////            }
////        }, ContextCompat.getMainExecutor(this))
////    }
////
////    /**
////     * Take the photo
////     */
////    private fun takePhoto() {
////
////    }
////
////    /**
////     * Request the camera permission from the system
////     */
////    private fun requestCameraPermission() {
////        when {
////            ContextCompat.checkSelfPermission(
////                this,
////                android.Manifest.permission.CAMERA
////            ) == PackageManager.PERMISSION_GRANTED -> {
////                Log.i("CaptureView", "Permission granted")
////            }
////
////            ActivityCompat.shouldShowRequestPermissionRationale(
////                this, android.Manifest.permission.CAMERA
////            ) -> Log.i("CaptureView", "Show permission dialog")
////
////            else -> requestPermissionLauncher.launch(android.Manifest.permission.CAMERA)
////        }
////    }
//
//    @Preview(showBackground = true, showSystemUi = true)
//    @Composable
//    private fun Camera(modifier: Modifier = Modifier) {
//        Text(
//            text = "Here's a camera",
//            modifier = modifier)
//    }
//}