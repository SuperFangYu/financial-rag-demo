package com.example.services;

import com.example.dto.AskRequest;
import com.example.dto.AskResponse;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@Service
public class RagClientService {

    private final RestTemplate restTemplate = new RestTemplate();

    public AskResponse queryRag(AskRequest request) {
        // 调用 FastAPI 接口
        String url = "http://127.0.0.1:8000/api/ask";
        return restTemplate.postForObject(url, request, AskResponse.class);
    }
}
