package me.send.model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
@Entity
public class Widget {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int id;
    private String name;
    private int height, width;
    private int x,y;
    @ManyToOne
    private Dashboard dashboard;
    @ManyToMany
    private List<WidgetData> widgetDataList;

    private enum GraphicType{
        ARRAY,
        BAR,
        LINE,
        DONUT,
        TEXT,
    }
}
