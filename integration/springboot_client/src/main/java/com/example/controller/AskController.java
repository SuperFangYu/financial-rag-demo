package com.example.controller;

import com.example.dto.AskRequest;
import com.example.dto.AskResponse;
import com.example.services.RagClientService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@Api(tags = "问答接口")
public class AskController {

    private final RagClientService ragClientService;

    // 构造器注入
    public AskController(RagClientService ragClientService) {
        this.ragClientService = ragClientService;
    }

    @PostMapping("/ask")
    @ApiOperation("调用 RAG 问答")
    public AskResponse ask(@RequestBody AskRequest request) {
        return ragClientService.queryRag(request);
    }
}
