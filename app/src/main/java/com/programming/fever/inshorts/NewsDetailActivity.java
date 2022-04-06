package com.programming.fever.inshorts;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.webkit.WebResourceRequest;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class NewsDetailActivity extends AppCompatActivity {

    String newslink;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_news_detail);

        //get data from intent
        Intent i =getIntent();
        newslink = i.getStringExtra("url");

        WebView view = (WebView)findViewById(R.id.webview);
        view.setWebViewClient(new WebViewClient(){
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                view.loadUrl(url);
                return false;
            }
        });
        view.getSettings().setJavaScriptEnabled(true);
        view.loadUrl(newslink);
    }
}
