from .vot import VOTDataset, VOTLTDataset
from .otb import OTBDataset
from .uav import UAVDataset
from .lasot import LaSOTDataset
from .nfs import NFSDataset
from .trackingnet import TrackingNetDataset
from .got10k import GOT10kDataset
from .dtb70 import DTB70Dataset
from .BlurryTrack import BlurryTrackDataset
class DatasetFactory(object):
    @staticmethod
    def create_dataset(**kwargs):
        """
        Args:
            name: dataset name 'OTB2015', 'LaSOT', 'UAV123', 'NFS240', 'NFS30',
                'VOT2018', 'VOT2016', 'VOT2018-LT'
            dataset_root: dataset root
            load_img: wether to load image
        Return:
            dataset
        """
        assert 'name' in kwargs, "should provide dataset name"
        name = kwargs['name']
        if 'OTB' in name:
            dataset = OTBDataset(**kwargs)
        elif 'LaSOT' == name:
            dataset = LaSOTDataset(**kwargs)
        elif 'UAV' in name:
            dataset = UAVDataset(**kwargs)
        elif 'NFS' in name:
            dataset = NFSDataset(**kwargs)
        elif 'VOT2018' == name or 'VOT2016' == name or 'VOT2019' == name:
            dataset = VOTDataset(**kwargs)
        elif 'VOT2018-LT' == name:
            dataset = VOTLTDataset(**kwargs)
        elif 'TrackingNet' == name:
            dataset = TrackingNetDataset(**kwargs)
        elif 'GOT-10k' == name:
            dataset = GOT10kDataset(**kwargs)
        elif 'DTB70_B' == name:
            dataset = DTB70Dataset(**kwargs)
        elif 'DTB70' == name:
            dataset = DTB70Dataset(**kwargs)
        elif 'DTB70_BM' == name:
            dataset = DTB70Dataset(**kwargs)
        elif 'OTB100_B' == name:
            dataset = OTBDataset(**kwargs)
        elif 'BlurryTrack' == name:
            dataset = BlurryTrackDataset(**kwargs)
        else:
            raise Exception("unknow dataset {}".format(kwargs['name']))
        return dataset

