package me.send.controller;

import me.send.model.Widget;
import me.send.service.UserService;
import me.send.service.WidgetService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RequestMapping("/widgets")
@RestController
public class WidgetController {

    private final WidgetService widgetService;

    public WidgetController(WidgetService widgetService) {
        this.widgetService = widgetService;
    }

    @GetMapping("")
    public ResponseEntity<List<Widget>> index(){
        return ResponseEntity.ok(widgetService.getList());
    }
}
