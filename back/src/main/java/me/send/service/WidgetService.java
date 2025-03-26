package me.send.service;

import me.send.model.Widget;
import me.send.model.repository.WidgetRepository;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

@Service
public class WidgetService {

    private final WidgetRepository widgetRepository;

    public WidgetService(WidgetRepository widgetRepository) {
        this.widgetRepository = widgetRepository;
    }

    public List<Widget> getList(){
        return StreamSupport.stream(widgetRepository.findAll().spliterator(), false)
                .toList();
    }

    public void create(){

    }
}
